var AddPublicOrdersOfGroupView = BaseView.extend({

    template: _.template($("#addPublicOrdersTemplate").html()),

    initialize: function(options) {
        this.group = options.group;
        this.collection = options.studentsCollection;
    },

    renderForm: function() {
        this.$('#addPublicOrdersForm').html(
            new AddPublicOrdersOfGroupFormView ({
                group: this.group,
                collection: this.collection
            }).render().el
        );
    },

    renderTable: function() {
        this.$('#addPublicOrdersTable').html(
            new AddPublicOrdersTableView({
                group: this.group
            }).render().el
        );
    },


    render: function() {
        this.$el.html(this.template(this.group.toJSON()));
        return this;
    }

});