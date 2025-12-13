# Age of Z Origins - 塔防遊戲

## 🎮 難度已調高
- 敵人數量增加 75%
- 敵人血量增加 50%
- 敵人速度提升
- 初始生命值：20 → 15
- 初始資源：300 → 250
- 獎勵金錢減少

## 🖼️ 如何更換底圖

### 方法1：修改背景顏色
在 `update()` 函數中找到這行：
```javascript
ctx.fillStyle = '#111'; ctx.fillRect(0,0,canvas.width, canvas.height);
```

改為：
```javascript
// 漸層背景
const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
gradient.addColorStop(0, '#0a0a0a');
gradient.addColorStop(0.5, '#1a1a1a'); 
gradient.addColorStop(1, '#0f0f0f');
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, canvas.width, canvas.height);
```

### 方法2：使用圖片背景
1. 準備圖片檔案 (建議 1920x1080)
2. 在 `<script>` 標籤前加入：
```html
<img id="bgImage" src="your-background.jpg" style="display:none;">
```

3. 在 `update()` 函數中替換背景繪製：
```javascript
const bgImg = document.getElementById('bgImage');
if(bgImg.complete) {
    ctx.drawImage(bgImg, 0, 0, canvas.width, canvas.height);
} else {
    ctx.fillStyle = '#111'; 
    ctx.fillRect(0,0,canvas.width, canvas.height);
}
```

### 方法3：添加廢土紋理
```javascript
// 在背景繪製後加入
ctx.fillStyle = 'rgba(40,40,40,0.3)';
for(let i = 0; i < 100; i++) {
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height;
    const size = Math.random() * 3 + 1;
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fill();
}
```

## 🎵 如何更換背景音樂

### 方法1：使用線上音樂
找到這行：
```html
<audio id="bgm" loop>
    <source src="https://cdn.pixabay.com/audio/2022/03/09/audio_c8c8a73467.mp3" type="audio/mpeg">
</audio>
```

替換為你的音樂URL：
```html
<audio id="bgm" loop>
    <source src="你的音樂網址.mp3" type="audio/mpeg">
</audio>
```

### 方法2：使用本地音樂檔案
1. 將音樂檔案放在同一資料夾
2. 修改為：
```html
<audio id="bgm" loop>
    <source src="./your-music.mp3" type="audio/mpeg">
    <source src="./your-music.ogg" type="audio/ogg">
</audio>
```

### 方法3：添加多首音樂隨機播放
```javascript
const musicList = [
    'music1.mp3',
    'music2.mp3', 
    'music3.mp3'
];

function playRandomMusic() {
    const bgm = document.getElementById('bgm');
    const randomIndex = Math.floor(Math.random() * musicList.length);
    bgm.src = musicList[randomIndex];
    bgm.volume = 0.2;
    bgm.play();
}

// 在 toggleMusic() 函數中使用
function toggleMusic() {
    if(!gameState.bgmStarted) {
        playRandomMusic();
        gameState.bgmStarted = true;
    }
}
```

## 🔊 推薦音樂來源
- **免費音樂**：Pixabay, Freesound, YouTube Audio Library
- **末日風格**：搜尋 "apocalypse", "zombie", "military", "dark ambient"
- **格式建議**：MP3 (相容性最佳)

## 🎨 推薦底圖風格
- 末日廢土場景
- 軍事基地俯視圖
- 破損的城市街道
- 荒涼的沙漠或雪地

記得調整圖片大小以避免影響遊戲效能！