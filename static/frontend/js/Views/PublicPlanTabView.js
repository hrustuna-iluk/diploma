var PublicPlanTabView = BaseView.extend({

    template: _.template($("#publicPlanTabTemplate").html()),

    collectionLen: 0,

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.group = options.group;
        this.collection.on('add', $.proxy(this._renderTr, this));
        this.collection.reset().fetch({data: {
            group: this.group.get('id')
        }});
    },

    _renderTr: function(model) {
        this.$('tbody').append(
            new PublicPlanTabElementView ({
                model: model
            }).render().el
        )
        this.$("table tbody tr:last td:first").text(++this.collectionLen);
    },

    render: function() {
        this.$el.html(this.template);
        return this;
    }

});