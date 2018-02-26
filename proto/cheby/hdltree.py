"""AST for the hdl description"""


class HDLNode(object):
    pass


class HDLModule(HDLNode):
    def __init__(self):
        self.name = None
        self.params = []
        self.ports = []
        self.signals = []
        self.stmts = []
        self.deps = []

    def add_dependence(self, name):
        if name not in self.deps:
            self.deps.append(name)


class HDLObject(HDLNode):
    def __init__(self, name=None, size=None, typ='L'):
        assert typ in "LUSI"  # Logic, Unsigned, Signed, Integer
        self.name = name
        self.size = size
        self.typ = typ
        self.comment = None
        assert size is None or isinstance(size, int)


class HDLSignal(HDLObject):
    pass


class HDLPort(HDLObject):
    def __init__(self, name=None, size=None, typ='L', dir='IN'):
        super(HDLPort, self).__init__(name, size, typ)
        self.dir = dir


class HDLParam(HDLObject):
    def __init__(self, name=None, size=None, typ='L', value=None):
        super(HDLParam, self).__init__(name, size, typ)
        self.value = value


class HDLStmt(HDLNode):
    pass


class HDLComment(HDLStmt):
    def __init__(self, comment):
        super(HDLComment, self).__init__()
        self.comment = comment


class HDLGenIf(HDLStmt):
    def __init__(self, cond):
        super(HDLGenIf, self).__init__()
        self.cond = cond
        self.stmts = []


class HDLAssign(HDLStmt):
    def __init__(self, target, expr):
        super(HDLAssign, self).__init__()
        self.target = target
        self.expr = expr


class HDLInstance(HDLStmt):
    def __init__(self, name, module_name):
        super(HDLInstance, self).__init__()
        self.name = name
        self.module_name = module_name
        self.params = []  # List of (name, expr).
        self.conns = []   # Ditto.


class HDLComb(HDLStmt):
    def __init__(self):
        super(HDLComb, self).__init__()
        self.stmts = []
        self.sensitivity = []


class HDLSync(HDLStmt):
    def __init__(self, clk, rst):
        super(HDLSync, self).__init__()
        self.clk = clk
        self.rst = rst
        self.rst_stmts = []
        self.sync_stmts = []


class HDLIfElse(HDLStmt):
    def __init__(self, cond):
        super(HDLIfElse, self).__init__()
        self.cond = cond
        self.then_stmts = []
        self.else_stmts = []


class HDLSwitch(HDLStmt):
    def __init__(self, expr):
        super(HDLSwitch, self).__init__()
        self.expr = expr
        self.choices = []


class HDLChoice(HDLNode):
    def __init__(self):
        super(HDLChoice, self).__init__()
        self.stmts = []


class HDLChoiceExpr(HDLChoice):
    def __init__(self, expr):
        super(HDLChoiceExpr, self).__init__()
        self.expr = expr


class HDLChoiceDefault(HDLChoice):
    pass


class HDLExpr(HDLNode):
    pass


class HDLCst(HDLExpr):
    pass


class HDLCstValue(HDLCst):
    def __init__(self, val):
        super(HDLCstValue, self).__init__()
        self.val = val


class HDLBit(HDLCstValue):
    pass


class HDLUndef(HDLCst):
    pass


bit_0 = HDLBit(0)
bit_1 = HDLBit(1)
bit_x = HDLUndef()


class HDLConst(HDLCst):
    def __init__(self, val, size):
        super(HDLConst, self).__init__()
        self.val = val
        self.size = size


class HDLNumber(HDLCstValue):
    pass


class HDLBool(HDLCstValue):
    pass


class HDLIndex(HDLExpr):
    def __init__(self, prefix, index):
        super(HDLIndex, self).__init__()
        self.prefix = prefix
        self.index = index


class HDLSlice(HDLExpr):
    def __init__(self, prefix, index, size=1):
        super(HDLSlice, self).__init__()
        self.prefix = prefix
        self.index = index
        self.size = size


class HDLReplicate(HDLExpr):
    def __init__(self, expr, num):
        super(HDLReplicate, self).__init__()
        self.expr = expr
        assert isinstance(num, int)
        self.num = num


class HDLUnary(HDLExpr):
    def __init__(self, expr):
        super(HDLUnary, self).__init__()
        self.expr = expr


class HDLNot(HDLUnary):
    pass


class HDLBinary(HDLExpr):
    def __init__(self, left, right):
        super(HDLBinary, self).__init__()
        self.left = left
        self.right = right


class HDLAnd(HDLBinary):
    pass


class HDLOr(HDLBinary):
    pass


class HDLEq(HDLBinary):
    pass