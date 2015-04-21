var PassesTableView = BaseView.extend({

    initialize: function (options) {
        this.week = options.week;
        this.faculty = options.faculty;
        this.semester = options.semester;
        this.passesCollection = options.passesCollection;
        this.studentsCollection = options.studentsCollection;
        this.classesCollection = options.classesCollection;
        this.$el = options.container;
    },

    _renderHeader: function () {
        this.headerView = new PassesTableHeadView({
            week: this.week,
            classesCollection: this.classesCollection,
            container: this.$el
        }).render();
    },

    _renderBody: function () {
        this.bodyView = new PassesTableBodyView({
            week: this.week,
            faculty: this.faculty,
            semester: this.semester,
            studentsCollection: this.studentsCollection,
            passesCollection: this.passesCollection,
            classesCollection: this.classesCollection,
            container: this.$el
        }).render();
    },

    render: function () {
        this._renderHeader();
        this._renderBody();
        return this;
    }
});