#version 330
in vec3 fragmentColor;
in vec2 fragmentTexCoord;
uniform sampler2D imageTexture;
out vec4 color;

const float THRESHOLD = 0.6;
const vec2 RESOLUTION = vec2(300.0, 300.0);

void main() {
    vec2 uv = vec2(fragmentTexCoord.x, 1.0 + fragmentTexCoord.y);

    vec4 base = texture(imageTexture, uv);

    vec3 bright = max(base.rgb - vec3(THRESHOLD), vec3(0.0));

    vec3 bloom = vec3(0.0);
    float samples = 0.0;
    for (int x = -2; x <= 2; x++) {
        for (int y = -2; y <= 2; y++) {
            vec2 offset = vec2(float(x), float(y)) / RESOLUTION;
            vec3 s = texture(imageTexture, uv + offset).rgb;
            bloom += max(s - vec3(THRESHOLD), vec3(0.0));
            samples += 1.0;
        }
    }
    bloom /= samples;

    color = vec4(base.rgb + bloom * 2, 1.0);
}