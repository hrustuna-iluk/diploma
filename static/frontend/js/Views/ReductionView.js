var ReductionView = BaseView.extend ({

    template:  _.template($("#reductionTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.passesCollection = options.passesCollection;
        this.studentsCollection = options.studentsCollection;
        this.classesCollection = options.classesCollection;
    },

    _attachEvents: function() {
        this.$('.firstSemesterJournal').on('click', $.proxy(this._firstSemester, this));
        this.$('.secondSemesterJournal').on('click', $.proxy(this._secondSemester, this));
    },

    _firstSemester: function() {},

    _secondSemester: function() {},

    render: function() {
        this.$el.html(this.template(_.extend(this.model.toJSON(), this.group.toJSON())));
        this._attachEvents();
        return this;
    }

});