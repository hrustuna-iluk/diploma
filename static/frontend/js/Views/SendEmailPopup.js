var SendMailPopupView = BaseView.extend({
    selectors: {
        message: '.message-text',
        send: '.sendEmail',
        close: '.closeModal'
    },

    template: _.template($('#sendMailPopupTemplate').html()),
    messageTemplate: _.template('<%=lastName%> <%=firstName%> <%=middleName%> у Вас перевищено ліміт пропусків. Наразі у Вас <%=passesAmount%> годин пропусків.'),

    events: function () {
        return _.invert({
            '_sendMail': 'click ' + this.selectors.send
        });
    },

    initialize: function (options) {
        this.student = options.student;
        this.passesAmount = options.passesAmount;
    },

    _sendMail: function () {
        var data = {
            student: this.student.get('id'),
            message: this.$(this.selectors.message).val()
        };

        $.post('/app/send_mail/', data, $.proxy(function (resp) {
            if (resp.success) {
                alert('Відправлено!');
                this.remove();
            } else {
                alert(resp.error);
            }
        }, this));
    },

    _fillText: function () {
        this.$(this.selectors.message).val(
            this.messageTemplate(_.extend(
                this.student.toJSON(),
                { passesAmount: this.passesAmount }
            ))
        );
    },

    render: function () {
        this.$el = $(this.template());
        this.delegateEvents();
        this._fillText();
        this.$el.modal('show');
        return this;
    }
});
