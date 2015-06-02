var SearchView = BaseView.extend({
    template: _.template($('#searchPage').html()),

    studentUserTemplate: _.template('<tr class="student" data-id="<%=id%>" data-query="<%=lastName%> <%=firstName%> <%=middleName%>">' +
        '<td><%=index%></td>' +
        '<td><%=lastName%></td>' +
        '<td><%=firstName%></td>' +
        '<td><%=middleName%></td>' +
        '<td><%=group.number%></td>' +
        '<td><%=email%></td>' +
        '<td><%=passesAmount%></td>' +
        '<td><button data-id="<%=id%>" data-passes="<%=passesAmount%>" class="send-email bg-darkTransparent"><i class="icon-mail fg-white"></i></button></td>' +
    '</tr>'),

    selectors: {
        searchField: '#search-student',
        studentsSearchList: '#students-search-list tbody',
        sendEmail: '.send-email'
    },

    events: function () {
        return _.invert({
            '_onSearch': 'input ' + this.selectors.searchField,
            '_onSendEmail': 'click ' + this.selectors.sendEmail,
            '_onClick': 'click tr'
        });
    },

    initialize: function (options) {
        this.departmentId = options.departmentId;
        this.passesCollection = options.passesCollection;
        this.classesCollection = options.classesCollection;
        this.studentsCollection = _.isArray(options.studentsCollection) ?
            new StudentsCollection(options.studentsCollection):
            options.studentsCollection;
    },

    _fillStudentsList: function (studentsList) {
        studentsList = studentsList ? new StudentsCollection(studentsList) : this.studentsCollection;
        this.$(this.selectors.studentsSearchList).empty();
        studentsList.each($.proxy(function (student, index) {
            var passesAmount = this.passesCollection.filter(function (pass) {
                return pass.get('student').id === +student.get('id');
            }).length;
            this.$(this.selectors.studentsSearchList).append(this.studentUserTemplate(
                _.extend(student.toJSON(), {index: index + 1, passesAmount: passesAmount * 2})
            ));
        }, this));
    },

    render: function () {
        this.$el.html(this.template());
        this._fillStudentsList();
        return this;
    },

    _closeModal: function() {
        this.remove();
        $('body').removeClass('modal-open');
        $('.modal-backdrop').hide();
    },

    _onSearch: function () {
        var query = this.$(this.selectors.searchField).val().toLowerCase();
        if (!query) {
            this._fillStudentsList();
            return
        }
        var studentsList = this.studentsCollection.filter(function (student) {
            return student.getFullName().toLowerCase().indexOf(query) > -1;
        });
        this._fillStudentsList(studentsList);
    },

    _onSendEmail: function (evt) {
        evt.stopPropagation();
        var student = this.studentsCollection.findWhere({ id: +$(evt.target).closest('button').data('id') });
        var passesAmount = $(evt.target).closest('button').data('passes');
        this.sendEmailModal = new SendMailPopupView({
            student: student,
            passesAmount: passesAmount
        }).render();
    },

    _onClick: function (evt) {
        var studId = $(evt.currentTarget).data('id');
        new StudentFiltersView({
            passesCollection: this.passesCollection,
            classesCollection: this.classesCollection,
            studentId: studId
        }).render().el;
    }
});