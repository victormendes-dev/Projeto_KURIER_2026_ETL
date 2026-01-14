from datetime import date, datetime

class Models:
    class LEADS:
        def __init__(
            self, lead_id: int,  created_at: date, status: str, contact_name: str = None, contact_email: str = None, contact_phone: str = None,
            marketing_channel: str = None, marketing_utm: str = None, metadata_score: int = None, metadata_duplicate: bool = None,
            metadata_test: bool = None
        ):
            self.lead_id            = lead_id
            self.created_at         = created_at
            self.status             = status
            self.contact_name       = contact_name
            self.contact_email      = contact_email
            self.contact_phone      = contact_phone
            self.marketing_channel  = marketing_channel
            self.marketing_utm      = marketing_utm
            self.metadata_score     = metadata_score
            self.metadata_duplicate = metadata_duplicate
            self.metadata_test      = metadata_test

        def to_tuple(self):
            return (
                self.lead_id,
                self.created_at,
                self.status,
                self.contact_name,
                self.contact_email,
                self.contact_phone,
                self.marketing_channel,
                self.marketing_utm,
                self.metadata_score,
                self.metadata_duplicate,
                self.metadata_test,
            )
    class CLIENTES:
        def __init__(
            self,  client_id: str, email: str, name_lead: str, converted_at: date, status: str, segment: str = None, internal_notes: str = None,
            origin_lead_id: str = None, origin_channel: str = None, owner_name: str = None, owner_team: str = None
        ):
            self.client_id       = client_id
            self.email           = email
            self.name_lead       = name_lead
            self.converted_at    = converted_at
            self.status          = status
            self.segment         = segment
            self.internal_notes  = internal_notes
            self.origin_lead_id  = origin_lead_id
            self.origin_channel  = origin_channel
            self.owner_name      = owner_name
            self.owner_team      = owner_team

        def to_tuple(self):
            return (
                self.client_id,
                self.email,
                self.name_lead,
                self.converted_at,
                self.status,
                self.segment,
                self.internal_notes,
                self.origin_lead_id,
                self.origin_channel,
                self.owner_name,
                self.owner_team,
            )
    class VENDAS: 
        def __init__(
            self, sale_id: str, client_id: str, sale_date: date, amount: int, status: str, product: str = None, payment_method: str = None,
            payment_installment: int = None, extra_discount: int = None, extra_notes: str = None
        ):
            self.sale_id             = sale_id
            self.client_id           = client_id
            self.sale_date           = sale_date
            self.amount              = amount
            self.status              = status
            self.product             = product
            self.payment_method      = payment_method
            self.payment_installment = payment_installment
            self.extra_discount      = extra_discount
            self.extra_notes         = extra_notes

        def to_tuple(self):
            return (
                self.sale_id,
                self.client_id,
                self.sale_date,
                self.amount,
                self.status,
                self.product,
                self.payment_method,
                self.payment_installment,
                self.extra_discount,
                self.extra_notes,
            )



