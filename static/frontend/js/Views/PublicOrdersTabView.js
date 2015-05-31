var PublicOrdersTabView = BaseView.extend({

    template: _.template($("#publicOrdersTabTemplate").html()),

    initialize: function(options) {
        this.model = options.group;
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});