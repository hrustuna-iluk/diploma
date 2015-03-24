var StudentAdditionalModalView = BaseView.extend({

    template: _.template($("#studentAdditionalModalTemplate").html()),

    initialize: function(options) {
        this.studentModel = options.studentModel;
    },

    _attachEvents: function() {
        this.$('.addAdditionalData').on('click', $.proxy(this._addAdditionalData, this));
        this.$('.closeModal').on('click', $.proxy(this._cancelModalWindow, this));
    },

    _addAdditionalData: function() {
        var additional = new AdditionalModel({
           title: this.$("#title").val(),
           value: this.$("#value").val()
        });
        this.studentModel.setAdditional(additional);
        this._cancelModalWindow();
    },

    _cancelModalWindow: function() {
        this.remove();
        $('body').removeClass('modal-open');
        $('.modal-backdrop').hide();
    },

    render: function() {
        this.$el = $(this.template());
        this.$el.modal('show');
        this._attachEvents();
        return this;
    }

});