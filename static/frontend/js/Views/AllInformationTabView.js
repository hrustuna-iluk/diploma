var AllInformationTabView = BaseView.extend({

    template: _.template($("#allInformationTabTemplate").html()),

    initialize: function(options) {
        this.collection = options.collection;
        this.group = options.group;
    },

    collectionLen: 0,

    _buildTable: function() {
        this.collection.reset().fetch({data: {
            group: this.group.get('id')
        },
            success: $.proxy(function () {
                this.collection.each($.proxy (function(item, index, array) {
                    this.$('tbody').append(
                        new AllInformationTabElementView ({
                            model: item
                        }).render().el
                    )
                    this.$('tbody tr:last td:first').text(++this.collectionLen);
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