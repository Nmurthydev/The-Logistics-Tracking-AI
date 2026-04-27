# modules/supply_chain.py
# supply_chain.py - placeholder functional code
# helpers for supply chain logic (simple placeholder)
def shipment_status_from_events(shipment_id, sess, shipments_table, events_table):
    # example: find last event where plate==assigned_plate for a shipment
    shipment = sess.execute(shipments_table.select().where(shipments_table.c.id==shipment_id)).fetchone()
    if not shipment:
        return {'shipment_id': shipment_id, 'status': 'not found'}
    plate = shipment.assigned_plate
    if not plate:
        return {'shipment_id': shipment_id, 'status': 'no plate assigned'}
    q = events_table.select().where(events_table.c.plate==plate).order_by(events_table.c.timestamp.desc()).limit(1)
    r = sess.execute(q).fetchone()
    if not r:
        return {'shipment_id': shipment_id, 'status':'no sightings'}
    return {'shipment_id': shipment_id, 'status':'in_transit', 'last_seen': str(r.timestamp), 'location': r.location}