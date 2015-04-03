var AllInformationTabElementView = BaseView.extend({

    tagName: 'tr',

    template: _.template($("#allInformationTabElementTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});