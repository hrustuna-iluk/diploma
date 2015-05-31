var PublicPlanTabElementView = BaseView.extend({

    tagName: 'tr',

    template: _.template($("#publicPlanTabElementTemplate").html()),

    selectors: {
        changePublicPlanButton: ".change-publicPlan",
        deletePublicPlanButton: ".remove-publicPlan"
    },

    _attachEvents: function() {
        this.$(this.selectors.changePublicPlanButton).on("click", $.proxy(this._changePublicPlan, this));
        this.$(this.selectors.deletePublicPlanButton).on("click", $.proxy(this._deletePublicPlan, this));
    },

    _changePublicPlan: function() {
        this.publisher.trigger('change:public:plan', this.model);
    },

    _deletePublicPlan: function() {
        this.remove();
    },


    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        this._attachEvents();
        return this;
    }

});