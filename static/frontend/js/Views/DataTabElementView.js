var DataTabElementView = BaseView.extend({

    tagName: 'tr',

    template: _.template($("#dataTabElementTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});

