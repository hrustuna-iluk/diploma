var WrapTabView = BaseView.extend({

    template: _.template($("#wrapTabTemplate").html()),

    initialize: function(options) {
        this.model = options.group;
    },

    render: function() {
        this.$el.html(this.template);
        return this;
    }

});