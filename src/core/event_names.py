"""
Core Event Definitions based on A1 Design Document.
This file serves as the single source of truth for all event types.
"""

# ==========================================
# 1. COMMAND EVENTS (CMD_)
# Requests from UI -> Logic/Server
# ==========================================

# Game Management
CMD_START_GAME = "CMD_START_GAME"
CMD_CONCEDE = "CMD_CONCEDE"

# Recruit Phase
CMD_BUY_MINION = "CMD_BUY_MINION"       # Payload: {target_index: int}
CMD_SELL_MINION = "CMD_SELL_MINION"     # Payload: {target_id: str}
CMD_PLAY_MINION = "CMD_PLAY_MINION"     # Payload: {hand_index: int, board_index: int}
CMD_REFRESH_SHOP = "CMD_REFRESH_SHOP"   # Payload: {}
CMD_FREEZE_SHOP = "CMD_FREEZE_SHOP"     # Payload: {}
CMD_TIER_UP = "CMD_TIER_UP"             # Payload: {}
CMD_REORDER_MINIONS = "CMD_REORDER_MINIONS" # Payload: {from_index: int, to_index: int}

# Hero & Discover
CMD_USE_HERO_POWER = "CMD_USE_HERO_POWER"
CMD_CHOOSE_DISCOVER = "CMD_CHOOSE_DISCOVER"

# ------------------------------------------
# Debug / Test (مخصوص توسعه)
# ------------------------------------------
CMD_DEBUG_DAMAGE = "CMD_DEBUG_DAMAGE"   # <--- ### این خط جا افتاده بود، حتما اضافه کن ###


# ==========================================
# 2. LOGIC / STATE EVENTS (EVENT_)
# Results from Logic -> UI
# ==========================================

# Minion State
EVENT_DAMAGE_TAKEN = "EVENT_DAMAGE_TAKEN"   # Payload: {target_id: str, amount: int}
EVENT_MINION_DIED = "EVENT_MINION_DIED"     # Payload: {target_id: str}
EVENT_MINION_SUMMONED = "EVENT_MINION_SUMMONED"
EVENT_STAT_BUFFED = "EVENT_STAT_BUFFED"
EVENT_DIVINE_SHIELD_LOST = "EVENT_DIVINE_SHIELD_LOST"

# Economy & Shop
EVENT_GOLD_UPDATED = "EVENT_GOLD_UPDATED"   # Payload: {current_gold: int}
EVENT_SHOP_REFRESHED = "EVENT_SHOP_REFRESHED" # Payload: {shop_minions: list}
EVENT_HAND_UPDATED = "EVENT_HAND_UPDATED"
EVENT_TIER_UPDATED = "EVENT_TIER_UPDATED"

# Combat Flow
EVENT_COMBAT_START = "EVENT_COMBAT_START"
EVENT_ATTACK_DECLARED = "EVENT_ATTACK_DECLARED" # Payload: {attacker_id: str, defender_id: str}
EVENT_COMBAT_RESULT = "EVENT_COMBAT_RESULT"

# Special Mechanics
EVENT_TRIPLE_FORMED = "EVENT_TRIPLE_FORMED"
EVENT_BATTLECRY_TRIGGERED = "EVENT_BATTLECRY_TRIGGERED"


# ==========================================
# 3. SYSTEM EVENTS (SYS_)
# Lifecycle & Meta-Game
# ==========================================
SYS_GAME_CONNECTED = "SYS_GAME_CONNECTED"
SYS_ERROR = "SYS_ERROR"                     # Payload: {message: str}
SYS_PHASE_CHANGED = "SYS_PHASE_CHANGED"     # Payload: {new_phase: str}
SYS_TURN_TIMER = "SYS_TURN_TIMER"           # Payload: {seconds_left: int}
SYS_ANIMATION_WAIT = "SYS_ANIMATION_WAIT"   # Payload: {duration: float}