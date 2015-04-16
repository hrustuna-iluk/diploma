var PassesTableBodyView = BaseView.extend({

    tagName: 'tr',

    initialize: function (options) {
        this.week = options.week;
        this.studentsCollection = options.studentsCollection;
        this.passesCollection = options.passesCollection;
        this.container = options.container;
    }
});