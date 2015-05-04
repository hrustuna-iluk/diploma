var PassesTableBodyView = BaseView.extend({

    MAX_CLASSES_PER_WEEK: 36,

    MAX_CLASSES_PER_DAY: 6,

    tagName: 'tbody',

    days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

    studentTemplate: _.template("<td><span><%=lastName%>&nbsp;<%=firstName%>&nbsp;<%=middleName%></span></td>"),

    initialize: function (options) {
        this.week = options.week;
        this.faculty = options.faculty;
        this.semester = options.semester;
        this.studentsCollection = options.studentsCollection;
        this.passesCollection = options.passesCollection;
        this.classesCollection = new ClassesCollection(options.classesCollection);
        this.container = options.container;
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

    _isEqualDate: function (date1, date2) {
        var firstDate = new Date(date1);
        var secondDate = new Date(date2);

        return firstDate.getDate() === secondDate.getDate() &&
               firstDate.getDay() === secondDate.getDay() &&
               firstDate.getMonth() === secondDate.getMonth() &&
               firstDate.getFullYear() === secondDate.getFullYear();
    },

    _renderStudents: function () {
        this.studentsCollection.reduce($.proxy(function ($body, student) {
            var $line = $('<tr>');
            var passes = this.passesCollection.filter(function (pass) {
                return pass.get('student').id === student.get('id');
            });
            $line = $line.
                append(this.studentTemplate(student.toJSON())).
                append(this._renderPasses(passes, student));
            return $body.add($line);
        }, this), $())
            .appendTo(this.$el);
    },

    _renderPasses: function (passes, student) {
        var $passes = $('<td colspan="6" class="passes"></td>');
        for (var i = 0; i < this.MAX_CLASSES_PER_WEEK; i++) {
            var weekDate = this._countStart(this.week.get('number'));
            var dayNumber = (i / this.MAX_CLASSES_PER_DAY) | 0;
            var classNumber = ((i % this.MAX_CLASSES_PER_DAY) | 0) + 1;
            weekDate.setDate(weekDate.getDate() + dayNumber);
            var pass = _.filter(passes, $.proxy(function (pass) {
                return pass.get('class_passed').day == this.days[dayNumber] &&
                       pass.get('class_passed').number == classNumber &&
                       pass.get('class_passed').numberOfWeek == this.week.get('numberOfWeek') &&
                       pass.get('class_passed').semester == this.semester &&
                       this._isEqualDate(weekDate, pass.get('date'));
            }, this));
            var classModel = this.classesCollection.findWhere({
                day: this.days[dayNumber],
                number: classNumber,
                numberOfWeek: this.week.get('numberOfWeek').toString(),
                semester: this.semester.toString()
            });
            if (!classModel) {
                $passes.append('<div class="pass"></div>');
                continue;
            }
            $passes = $passes.append(
                new PassView({
                    class: classModel,
                    passesCollection: this.passesCollection,
                    student: student,
                    date: weekDate,
                    model: pass[0]
                }).render().el
            )
        }
        return $passes;
    },

    render: function () {
        this._renderStudents();
        this.container.find(this.tagName).remove();
        this.container.append(this.$el);
        return this;
    }
});