var ReportTabElementView = BaseView.extend({

    tagName: "tr",

    template: _.template($("#reportTabElementTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});