var PublicEventsTabView = BaseView.extend({

    template: _.template($("#publicEventsTabTemplate").html()),

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.group = options.group;
        this.collection.on('add', $.proxy(this._renderTr, this));
        //this.collection.reset().fetch();
    },

    _renderTr: function(model) {
        if(model.getSemester() === 1) {
            this.$('.firstTable tbody').append(
                new PublicEventsTabElementView({
                    model: model
                }).render().el
            )
        } else {
            this.$('.secondTable tbody').append(
                new PublicEventsTabElementView({
                    model: model
                }).render().el
            )
        }
    },

    render: function() {
        this.$el.html(this.template);
        return this;
    }

});