var DataTabView = BaseView.extend({

    template: _.template($("#dataTabTemplate").html()),

    collectionLen: 0,

    initialize: function(options) {
        this.group = options.group;
        this.collection = options.collection;
    },

    _buildTable: function() {
        this.collection.reset().fetch({data: {
            group: this.group.get('id')
        },
        success: $.proxy(function () {
                this.collection.each($.proxy (function(item, index, array) {
                    this.$('tbody').append(
                        new DataTabElementView ({
                            model: item
                        }).render().el
                    )
                    this.$("table tbody tr:last td:first").text(++this.collectionLen);
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