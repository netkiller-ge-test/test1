// WebSocket 기반 실시간 알림 전송 서비스
class NotificationService {
    constructor(serverUrl) {
        this.serverUrl = serverUrl;
        this.connected = false;
        this.queue = [];
    }

    connect() {
        console.log(`Connecting to notification server: ${this.serverUrl}`);
        this.connected = true;
        this.processQueue();
    }

    sendNotification(userId, message, priority = 'NORMAL') {
        const payload = {
            userId,
            message,
            priority,
            timestamp: new Date().toISOString()
        };

        if (!this.connected) {
            console.warn("Server not connected. Queueing message...");
            this.queue.push(payload);
            return false;
        }

        console.log(`[${priority}] Notification sent to User ${userId}: ${message}`);
        return true;
    }

    processQueue() {
        while (this.queue.length > 0) {
            const payload = this.queue.shift();
            this.sendNotification(payload.userId, payload.message, payload.priority);
        }
    }
}

module.exports = NotificationService;
