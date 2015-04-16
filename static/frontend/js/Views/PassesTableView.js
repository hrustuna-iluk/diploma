var PassesTableView = BaseView.extend({

    initialize: function (options) {
        this.week = options.week;
        this.passesCollection = options.passesCollection;
        this.studentsCollection = options.studentsCollection;
        this.classesCollection = options.classesCollection;
        this.$el = options.container;
    },

    _renderHeader: function () {
        this.headerView = new PassesTableHeadView({
            week: this.week,
            classesCollection: this.classesCollection,
            container: this.$el.find('thead')
        }).render();
    },

    _renderBody: function () {
        this.bodyView = new PassesTableBodyView({
            studentsCollection: this.studentsCollection,
            passesCollection: this.passesCollection,
            container: this.$el.find('tbody')
        }).render();
    },

    render: function () {
        this._renderHeader();
        //this._renderBody();
        return this;
    }
});