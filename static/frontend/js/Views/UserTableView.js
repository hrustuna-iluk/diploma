var UserTableView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#userTableTemplate").html()),

    _attachEvents: function() {
        this.$('.remove-user-data').on('click', $.proxy(this._removeUser, this));
        this.$('#userAccess').on('click', $.proxy(this._changeActivity, this));
    },

    _removeUser: function() {
        if(this.$('#userAccess').val()) {
            this.model.get('user').set('isActive', true);
            this.model.save();
            return;
        }
         this.model.get('user').set('isActive', false);
         this.model.save();
    },

    _changeActivity: function() {

    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});
