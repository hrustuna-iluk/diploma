var TeacherView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#teacherTemplate").html()),

    selectors: {
        changeTeacherData: ".change-teacher-data",
        deleteTeacherData: ".remove-teacher-data"
    },

    initialize: function() {
        this.model.on('change', $.proxy(this.render, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.changeTeacherData).on("click", $.proxy(this._changeTeacherData, this));
        this.$(this.selectors.deleteTeacherData).on("click", $.proxy(this._deleteTeacherData, this));
    },

    _changeTeacherData: function() {
        this.publisher.trigger('change:teacher', this.model);
    },

    _deleteTeacherData: function() {
        this.model.destroy();
        this.remove();
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }
});