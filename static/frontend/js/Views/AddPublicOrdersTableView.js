var AddPublicOrdersTableView = BaseView.extend({

    template: _.template($("#addPublicOrdersTableTemplate").html()),

    initialize: function(options) {
        this.model = options.group;
        this.model.on('change', $.proxy(this.render, this));
    },

    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }

});