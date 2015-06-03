var PassesTableHeadView = BaseView.extend({

    tagName: 'thead',

    MAX_CLASS_AMOUNT: 6,

    dayTemplate: _.template(
        "<td>" +
            "<div class='classes'><%=classes%></div>" +
            "<div class='date'><%=date%></div>" +
            "<div class='day' ><%=day%></div>" +
        "</td>"
    ),

    classTemplate: _.template("<div class='class'><span class='ellipsis'><%=subject%></span></div>"),

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    daysUkraine: {
        Monday: 'Понеділок',
        Tuesday: 'Вівторок',
        Wednesday: 'Середа',
        Thursday: 'Четвер',
        Friday: "П'ятниця",
        Saturday: 'Субота'
    },

    initialize: function (options) {
        this.week = options.week;
        this.classesCollection = new ClassesCollection(options.classesCollection);
        this.container = options.container;
    },

    _renderDays: function () {
        var $line = $('<tr>');
        var start = this.week.get('start').valueOf();
        this.days.forEach($.proxy(function (day, index) {
            var startDate = new Date(start);
            var date = new Date( startDate.setDate( startDate.getDate() + index ) );
            var $day = this._renderDay(day, date);
            $line.append($day);
        }, this));
        $line.prepend($('<td>'));
        this.$el.append($line)
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
        for (var i = 1; i <= this.MAX_CLASS_AMOUNT; i++ ) {
            var pass = null;
            var classItem = classes.findWhere({
                number: i
            });
            var $class = classItem ?
                    this.classTemplate(classItem.toJSON()) :
                    this.classTemplate({  subject: '&nbsp;' });
            $el = $el.add(
                classItem ?
                    this.classTemplate(classItem.toJSON()) :
                    this.classTemplate({  subject: '&nbsp;' })
            );
        }

        return this.dayTemplate({
            classes: $('<div>').append($el).html(),
            day: this.daysUkraine[day],
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
            day: this.daysUkraine[day],
            date: date.toLocaleString().split(',')[0]
        });
    },

    render: function () {
        this._renderDays();
        this.container.find(this.tagName).remove();
        this.container.append(this.$el);
        return this;
    }
});