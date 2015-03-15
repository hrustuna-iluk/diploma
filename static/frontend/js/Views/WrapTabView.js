var WrapTabView = BaseView.extend({

    template: _.template($("#groupTemplate").html()),

    render: function() {
        this.$el.html(this.template);
        return this;
    }

});