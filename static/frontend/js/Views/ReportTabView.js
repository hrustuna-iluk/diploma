var ReportTabView = BaseView.extend({

    template: _.template($("#reportTabTemplate").html()),

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.group = options.group;
    },

    _buildTable: function() {
        this.collection.reset().fetch({
            data: {
                group: this.group.get('id')
            },
            success: $.proxy(function () {
                this.collection.each($.proxy (function(item, index, array) {
                    this.$('tbody').append(
                        new ReportTabElementView ({
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