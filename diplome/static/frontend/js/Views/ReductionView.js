var ReductionView = BaseView.extend ({

    template:  _.template($("#reductionTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.faculty = options.faculty;
        this.passesCollection = options.passesCollection;
        this.studentsCollection = options.studentsCollection;
        this.classesCollection = options.classesCollection;
    },

    _renderSubViews: function () {
        this.firstSemesterPagination = new PaginationsView({
            container: this.$('#firstSemesterJournal .paginationJournal nav'),
            faculty: this.faculty,
            semester: 1
        }).render();

        this.secondSemesterPagination = new PaginationsView({
            container: this.$('#secondSemesterJournal .paginationJournal nav'),
            faculty: this.faculty,
            semester: 2
        }).render();
    },

    _attachEvents: function() {
        this.publisher.on('pagination:item:clicked', $.proxy(function (semester, week) {
            var container = semester == 1 ? this.$('#firstSemesterJournal table') : this.$('#secondSemesterJournal table');
            this.passesView = new PassesTableView({
                week: week,
                faculty: this.faculty,
                semester: semester,
                passesCollection: this.passesCollection,
                studentsCollection: this.studentsCollection,
                classesCollection: this.classesCollection.where({ semester: semester.toString() }),
                container: container
            }).render();
        }, this));
    },

    _showFirstPage: function () {
        this.publisher.trigger('passes:paginator:show:page', 1);
    },

    render: function() {
        this.$el.html(this.template(this.group.toJSON()));
        this._renderSubViews();
        this._attachEvents();
        this._showFirstPage();
        return this;
    }

});