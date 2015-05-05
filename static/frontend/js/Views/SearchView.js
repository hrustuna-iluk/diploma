var SearchView = BaseView.extend({
    template: _.template($('#searchPage').html()),

    studentUserTemplate: _.template('<tr class="student" data-query="<%=lastName%> <%=firstName%> <%=middleName%>">' +
        '<td><%=index%></td>' +
        '<td><%=lastName%></td>' +
        '<td><%=firstName%></td>' +
        '<td><%=middleName%></td>' +
        '<td><%=group.number%></td>' +
        '<td><%=email%></td>' +
        '<td><%=passesAmount%></td>' +
        '<td><button data-id="<%=id%>" data-passes="<%=passesAmount%>" class="send-email bg-darkTransparent"><i class="icon-remove fg-white"></i></button></td>' +
    '</tr>'),

    selectors: {
        searchField: '#search-student',
        studentsSearchList: '#students-search-list tbody',
        sendEmail: '.send-email'
    },

    events: function () {
        return _.invert({
            '_onSearch': 'input ' + this.selectors.searchField,
            '_onSendEmail': 'click ' + this.selectors.sendEmail
        });
    },

    initialize: function (options) {
        this.departmentId = options.departmentId;
        this.passesCollection = options.passesCollection;
        this.studentsCollection = _.isArray(options.studentsCollection) ?
            new StudentsCollection(options.studentsCollection):
            options.studentsCollection;
    },

    _fillStudentsList: function () {
        this.$(this.selectors.studentsSearchList).empty();
        this.studentsCollection.each($.proxy(function (student, index) {
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

    _onSearch: function () {
        var query = this.$(this.selectors.searchField).val();
        this.$(this.selectors.studentsSearchList).empty();
        this.$('tr.student').each(function () {

        });
    },

    _onSendEmail: function (evt) {
        var student = this.studentsCollection.findWhere({ id: +$(evt.target).closest('button').data('id') });
        var passesAmount = $(evt.target).closest('button').data('passes');
        this.sendEmailModal = new SendMailPopupView({
            student: student,
            passesAmount: passesAmount
        }).render();
    }
});