var ReportTabView = BaseView.extend({

    template: _.template($("#allInformationTabTemplate").html()),

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.group = options.group;
    },

    _buildTable: function() {
        this.collection.reset().fetch({
            success: $.proxy(function () {
                this.collection.each($.proxy (function(item, index, array) {
                    this.$('tbody').append(
                        new AllInformationTabElementView ({
                            model: item
                        }).render().el
                    )
                }, this));
            }, this)
        });
    },

    render: function() {
        this.$el.html(this.template);
        this._buildTable();
        return this;
    }

});