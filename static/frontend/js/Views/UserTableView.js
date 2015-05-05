var UserTableView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#userTableTemplate").html()),

    initialize: function (options) {
        this.index = options.index;
    },

    _attachEvents: function() {
        this.$('#userAccess').off().on('click', $.proxy(this._changeActivity, this));
    },

    _changeActivity: function() {
        var checked = this.$('#userAccess').is(':checked');
        this.model.get('user').is_active = checked;
        this.model.save();
        this.render();
    },

    render: function() {
        this.$el.html(this.template(_.extend(this.model.toJSON(), {index: this.index})));
        this._attachEvents();
        return this;
    }

});
