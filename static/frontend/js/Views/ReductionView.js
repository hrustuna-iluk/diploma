var ReductionView = BaseView.extend ({

    template:  _.template($("#reductionTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.faculty = options.faculty;
        this.passesCollection = options.passesCollection;
        this.studentsCollection = options.studentsCollection;
        this.classesCollection = options.classesCollection;
    },

    firstSemester: null,

    secondSemester: null,

    _attachEvents: function() {
        this.$('.firstSemesterJournal').on('click', $.proxy(this._firstSemester, this));
        this.$('.secondSemesterJournal').on('click', $.proxy(this._secondSemester, this));
    },

    _firstSemester: function() {
        this.secondSemester = null;
        this.$('#firstSemesterJournal .paginationJournal nav').html(
            this.firstSemester = new PaginationsView({
                faculty: this.faculty,
                semester: 1
            }).render().el
        );
    },

    _secondSemester: function() {
        this.firstSemester = null;
        this.$('#secondSemesterJournal .paginationJournal nav').html(
            this.secondSemester = new PaginationsView({
                faculty: this.faculty,
                semester: 2
            }).render().el
        );
    },

    render: function() {
        this.$el.html(this.template(_.extend(this.model.toJSON(), this.group.toJSON())));
        this._attachEvents();
        return this;
    }

});