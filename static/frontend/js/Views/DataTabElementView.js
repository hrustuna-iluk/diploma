var DataTabElementView = BaseView.extend({

    template: _.template($("#dataTabElementTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});

