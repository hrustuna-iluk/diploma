var ReportTabElementView = BaseView.extend({

    template: _.template($("#reportTabElementTemplate").html()),

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});