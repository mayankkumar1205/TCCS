from ConsignmentStatus import ConsignmentStatus
from app import db

join_table = db.Table('join_table', db.BASE.metadata,
                     db.Column('consignmentID', db.Integer, db.ForeignKey('Consignment.consignmentID')),
                     db.Column('truckID', db.Integer, db.ForeignKey('Truck.truckID')))

class Consignment:
    consignmentID = db.Column(db.Integer, primary_key=True)
    volume = db.Column(db.Integer, index=True)
    senderAddress = db.relationship('Address', uselist=False, lazy=False)
    receiverAddress = db.relationship('Address', uselist=False, lazy=False)
    status = db.Column(db.Integer, index=True)
    sourceBranch = db.Column(db.String(64), index=True)
    destinationBranch = db.Column(db.String(64), index=True)
    truckID = db.relationship("Truck", secondary=join_table, back_populates="consignments")
    charge = db.Column(db.Integer, index=True)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def __repr__(self) -> str:
        return f'< ID: {self.consignmentID} Volume: {self.volume} Status: {self.status} Sender Address: {self.senderAddress} \
            Receiver Address: {self.receiverAddress} Status: {ConsignmentStatus(self.status)} Source Branch: {self.sourceBranch} \
            Destination Branch: {self.destinationBranch} Charge: {self.charge}>'
    
    def getConsignmentID(self):
        return self.consignmentID
    def getVolume(self):
        return self.volume
    def getSenderAddress(self):
        return self.senderAddress
    def getReceiverAddress(self):
        return self.receiverAddress
    def getStatus(self):
        return self.status
    def getSourceBranch(self):
        return self.sourceBranch
    def getDestinationBranch(self):
        return self.destinationBranch
    def getTruckID(self):
        return self.truckID
    def getCharge(self):
        return self.charge
    
    def setVolume(self, a):
        self.volume = a
    def setSenderAddress(self, e):
        self.senderAddress = e
    def setReceiverAddress(self, e):
        self.senderAddress = e
    def setStatus(self, e):
        self.status = e
    def setSourceBranch(self, e):
        self.sourceBranch = e
    def setDestinationBranch(self, e):
        self.destinationBranch = e