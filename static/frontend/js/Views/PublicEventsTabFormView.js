var PublicEventsTabFormView = BaseView.extend({

    template: _.template($("#publicEventsTabFormTemplate").html()),

    optionPublicEventTemplate: _.template($("#optionPublicEventTemplate").html()),

    selectors: {
        publicEventSelect: '#publicEvent',
        publicSemesterSelect: '#semester',
        publicAmountHours: '#amountHours',
        publicAmountPresent: '#amountPresent',
        createEventButton: '#addPublicEvent',
        changeEventButton: '#changePublicEvent'
    },

    initialize: function(options) {
        this.collection = options.publicPlanCollection;
        this.group = options.group;
        this.publisher.on('change:public:event', $.proxy(this._onPublicEventChange, this));
        this.collection.reset().fetch({data: {
            group: this.group.get('id')
        },
            success: $.proxy(this._fillEventList, this)
        });
    },

    _attachEvents: function() {
        this.$(this.selectors.createEventButton).on('click', $.proxy(this._createPublicEvent, this));
        this.$(this.selectors.changeEventButton).on('click', $.proxy(this._changePublicEvent, this));
    },

    _onPublicEventChange: function(model) {
        $(this.selectors.publicEventSelect).val(model.getEvent());
        $(this.selectors.publicSemesterSelect).val(model.getSemester());
        $(this.selectors.publicAmountHours).val(model.getAmountHours());
        $(this.selectors.publicAmountPresent).val(model.getAmountPresent());
        this.$(this.selectors.changeEventButton).data('model', model);
        this.$(this.selectors.createEventButton).addClass('no-display');
        this.$(this.selectors.changeEventButton).removeClass('no-display');
    },

    _publicEventData: function(model) {
        model.setSemester(+this.$(this.selectors.publicSemesterSelect).val());
        model.setAmountHours(this.$(this.selectors.publicAmountHours).val());
        model.setAmountPresent(this.$(this.selectors.publicAmountPresent).val());
        this.$(this.selectors.publicEventSelect).find('option:first').attr('selected', true);
        this.$(this.selectors.publicSemesterSelect).find('option:first').attr('selected', true);
        this.$(this.selectors.publicAmountHours).val("");
        this.$(this.selectors.publicAmountPresent).val("");
    },

    _createPublicEvent: function() {
        var publicEventModel = this.collection.findWhere({id: +this.$(this.selectors.publicEventSelect).val()});
        this._publicEventData(publicEventModel);
        publicEventModel.save();
    },

    _changePublicPlan: function() {
        var publicEventModel = this.$(this.selectors.changeEventButton).data('model');
        this._publicEventData(publicEventModel);
        publicEventModel.save();
        this.$(this.selectors.changeEventButton).addClass('no-display');
        this.$(this.selectors.createEventButton).removeClass('no-display');
    },

    _fillEventList: function() {
        this.collection.each(function(model) {
            this.$('#publicEvent').append(this.optionPublicEventTemplate(model.toJSON()));
        }, this);
    },

    render: function() {
        this.$el.html(this.template);
        this._attachEvents();
        return this;
    }

});