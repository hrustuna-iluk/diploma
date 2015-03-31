var StudentView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#studentTemplate").html()),

    selectors: {
        changeStudentData: ".change-student-data",
        deleteStudentData: ".remove-student-data"
    },

    initialize: function() {
        this.model.on('change', $.proxy(this.render, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.changeStudentData).on("click", $.proxy(this._changeStudentData, this));
        this.$(this.selectors.deleteStudentData).on("click", $.proxy(this._deleteStudentData, this));
    },

    _changeStudentData: function() {
        this.publisher.trigger('change:student', this.model);
    },

    _deleteStudentData: function() {
        this.remove();
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }
});
