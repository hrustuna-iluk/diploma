var PaginationView = BaseView.extend({

    tagName: 'li',

    template: _.template('<a style="color:#337ab7;" href="javascript:void 0"><%=number%></a>'),

    initialize: function(options) {
        this.collection = options.collection;
        this.semester = options.semester;
        this.faculty = options.faculty;
        this._addPaginationModel();
    },

    events: {
        'click': '_onClick'
    },

    _countStart: function(week) {
        var startSemester = this.semester == 1 ? this.faculty.get('startFirstSemester') : this.faculty.get('startSecondSemester');
        var year = new Date().getFullYear();
        var offset = week * 7 * 24 * 60 * 60 * 1000;
        var startOfCurrentYear = new Date(startSemester);
        var date = new Date(startOfCurrentYear.valueOf() + offset);
        var day = date.getDay();

        if (day !== 1) {
            date.setDate( day === 0 ? date.getDate() + 1 : date.getDate() - (day - 1) );
        }
        return date;
    },

    _countEnd: function(week) {
        var endSemester = this.semester == 1 ? this.faculty.get('endFirstSemester') : this.faculty.get('endSecondSemester');
        var year = new Date().getFullYear();
        var offset = week * 7 * 24 * 60 * 60 * 1000;
        var startOfCurrentYear = new Date(endSemester);
        var date = new Date(startOfCurrentYear.valueOf() + offset);
        var day = date.getDay();

        if (day !== 6) {
            date.setDate( date.getDate() + (6 - day) );
        }
        return date;
    },

    _countWeek: function() {
        return this.collection.length % 2 ? 2 : 1;
    },

    _addPaginationModel: function() {
        var week = this._countWeek();
        var number = this.collection.length;
        this.model = new PaginationModel({
            number: number,
            numberOfWeek: week,
            start: this._countStart(number),
            end: this._countEnd(number)
        });
        this.collection.add(this.model);
    },

    _onClick: function () {
      this.publisher.trigger('pagination:item:clicked', this.semester, this.model);
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});