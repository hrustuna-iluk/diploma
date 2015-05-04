var UserTableView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#userTableTemplate").html()),

    _attachEvents: function() {
        this.$('.remove-user-data').off().on('click', $.proxy(this._removeUser, this));
        this.$('#userAccess').off().on('click', $.proxy(this._changeActivity, this));
    },

    _removeUser: function() {
        this.model.get('user').is_active = false;
        this.model.save();
        this.render();
    },

    _changeActivity: function() {
        var checked = this.$('#userAccess').is(':checked');
        this.model.get('user').is_active = checked;
        this.model.save();
        this.render();
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});
