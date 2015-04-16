var PassesTableHeadView = BaseView.extend({

    tagName: 'tr',

    MAX_CLASS_AMOUNT: 6,

    dayTemplate: _.template(
        "<td>" +
            "<div class='classes'><%=classes%></div>" +
            "<div class='date'><%=date%></div>" +
            "<div class='day' ><%=day%></div>" +
        "</td>"
    ),

    classTemplate: _.template("<div class='class'><span><%=subject%></span></div>"),

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

    initialize: function (options) {
        this.week = options.week;
        this.classesCollection = new ClassesCollection(options.classesCollection);
        this.container = options.container;
    },

    _renderDays: function () {
        var start = this.week.get('start').valueOf();
        this.days.forEach($.proxy(function (day, index) {
            var startDate = new Date(start);
            var date = new Date( startDate.setDate( startDate.getDate() + index ) );
            var $day = this._renderDay(day, date);
            this.$el.append($day);
        }, this));
    },

    _renderDay: function (day, date) {
        var $el = $();
        var classes = this.classesCollection.where({
            day: day,
            numberOfWeek: this.week.get('numberOfWeek').toString()
        });

        if (!classes.length) {
            return this._emptyDay(day, date);
        }
        classes = new ClassesCollection(classes);
        for (var i=1; i <= this.MAX_CLASS_AMOUNT; i++ ) {
            var $class = null;
            var classItem = classes.findWhere({
                number: i
            });
            $el = $el.add(
                classItem ?
                    this.classTemplate(classItem.toJSON()) :
                    this.classTemplate({  subject: '&nbsp;' })
            );
        }

        return this.dayTemplate({
            classes: $('<div>').append($el).html(),
            day: day,
            date: date.toLocaleString().split(',')[0]
        });
    },

    _emptyDay: function (day, date) {
        var $classes = $();

        for (var i=0; i < this.MAX_CLASS_AMOUNT; i++ ) {
          $classes = $classes.add(this.classTemplate({
              subject: '&nbsp;'
          }))
        }
        return this.dayTemplate({
            classes: $('<div>').append($classes).html(),
            day: day,
            date: date.toLocaleString().split(',')[0]
        });
    },

    render: function () {
        this._renderDays();
        this.container.html(this.$el);
        return this;
    }
});