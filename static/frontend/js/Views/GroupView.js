var GroupView = BaseView.extend({

    template: _.template($("#groupTemplate").html()),

    selectors: {
        changeGroup: ".change-group",
        deleteGroup: ".remove-group"
    },

    _attachEvents: function() {
        this.$(this.selectors.changeGroup).off().on("click", $.proxy(this._changeGroup, this));
        this.$(this.selectors.deleteGroup).off().on("click", $.proxy(this._deleteGroup, this));
        this.model.on('change', $.proxy(this.render, this));
    },

    _changeGroup: function() {
        this.publisher.trigger('change:group', this.model);
    },

    _deleteGroup: function() {
        this.model.destroy();
        this.remove();
    },

    render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }
});