var DepartmentView = BaseView.extend ({

    template: _.template($("#newDepartmentTemplate").html()),

    selectors: {
        changeDepartment: ".change-department",
        deleteDepartment: ".remove-department"
    },

    initialize: function() {
        this.model.on('change', $.proxy(this.render, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.changeDepartment).on("click", $.proxy(this._changeDepartment, this));
        this.$(this.selectors.deleteDepartment).on("click", $.proxy(this._deleteDepartment, this));
    },

    _changeDepartment: function() {
        this.publisher.trigger('change:department', this.model);
    },

    _deleteDepartment: function() {
        this.model.destroy();
        this.remove();
    },

    render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }
});