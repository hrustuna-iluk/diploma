var TabView = BaseView.extend({

    template: _.template($("#tabTemplate").html()),

    render: function() {
        this.$el.html(this.template);
        return this;
    }

});