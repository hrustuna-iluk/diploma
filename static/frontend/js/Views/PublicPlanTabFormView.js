var PublicPlanTabFormView = BaseView.extend({

    template: _.template($("#publicPlanTabFormTemplate").html()),

    selectors: {
        publicPlanEventInput: '#publicPlanEvent',
        publicPlanDateInput: '#publicPlanDate',
        publicPlanResponsiveInput: '#publicPlanResponsive',
        publicPlanDescriptionInput: '#publicPlanDescription',
        createPlanButton: '#addPublicPlan',
        changePlanButton: '#changePublicPlan'
    },

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.publisher.on('change public plan', $.proxy(this._onPublicPlanChange, this));
    },

    _attachEvents: function() {
        this.$(this.selectors.createPlanButton).on('click', $.proxy(this._createPublicPlan, this));
        this.$(this.selectors.changePlanButton).on('click', $.proxy(this._changePublicPlan, this));
    },

    _onPublicPlanChange: function(model) {
        $(this.selectors.publicPlanEventInput).val(model.getEvent());
        $(this.selectors.publicPlanDateInput).val(model.getDate());
        $(this.selectors.publicPlanResponsiveInput).val(model.getResponsive());
        $(this.selectors.publicPlanDescriptionInput).val(model.getDescription());
        this.$(this.selectors.changePlanButton).data('model', model);
        this.$(this.selectors.createPlanButton).addClass('no-display');
        this.$(this.selectors.changePlanButton).removeClass('no-display');
    },

    _publicPlanData: function(model) {
        model.setEvent(this.$(this.selectors.publicPlanEventInput).val());
        model.setDate(this.$(this.selectors.publicPlanDateInput).val());
        model.setResponsive(this.$(this.selectors.publicPlanResponsiveInput).val());
        model.setDescription(this.$(this.selectors.publicPlanDescriptionInput).val());
        this.$(this.selectors.publicPlanEventInput).val("");
        this.$(this.selectors.publicPlanDateInput).val("");
        this.$(this.selectors.publicPlanResponsiveInput).val("");
        this.$(this.selectors.publicPlanDescriptionInput).val("");
    },

    _createPublicPlan: function() {
        var publicPlanModel = new PublicPlanModel();
        this._publicPlanData(publicPlanModel);
        publicPlanModel.save({wait: true}, {success: $.proxy(function() {
                    this.collection.add(publicPlanModel);
                }, this)})
    },

    _changePublicPlan: function() {
        var publicPlanModel = this.$(this.selectors.changePlanButton).data('model');
        this._publicPlanData(publicPlanModel);
        publicPlanModel.save();
        this.$(this.selectors.changePlanButton).addClass('no-display');
        this.$(this.selectors.createPlanButton).removeClass('no-display');
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }

});