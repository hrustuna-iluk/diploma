var PublicOrdersTabView = BaseView.extend({

    template: _.template($("#publicOrdersTabTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});