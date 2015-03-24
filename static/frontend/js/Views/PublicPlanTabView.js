var PublicPlanTabView = BaseView.extend({

    template: _.template($("#publicPlanTabTemplate").html()),

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.group = options.group;
        this.collection.on('add', $.proxy(this._renderTr, this));
        //this.collection.reset().fetch();
    },

    _renderTr: function(model) {
        this.$('tbody').append(
            new PublicPlanTabElementView ({
                model: model
            }).render().el
        )
    },

    render: function() {
        this.$el.html(this.template);
        return this;
    }

});