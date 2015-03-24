var DataTabView = BaseView.extend({

    template: _.template($("#dataTabTemplate").html()),

    initialize: function(options) {
        this.collection = options.collection;
    },

    _buildTable: function() {
        this.collection.reset().fetch({
            success: $.proxy(function () {
                this.collection.each($.proxy (function(item, index, array) {
                    this.$('tbody').append(
                        new DataTabElementView ({
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