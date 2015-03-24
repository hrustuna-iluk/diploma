var AllInformationTabElementView = BaseView.extend({

    template: _.template($("#allInformationTabElementTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});