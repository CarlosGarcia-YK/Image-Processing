% Definir puntos básicos que representan un símbolo π aproximado
x = [1, 3, 3, 2, 2, 4, 4, 3, 3, 5];
y = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1];

% Número de puntos en el contorno
N = length(x);

% Calcular los coeficientes de Fourier
X = fft(x);
Y = fft(y);

% Preparar la figura para la animación
figure;
hold on;
axis equal;
xlim([0, 6]);
ylim([0, 3]);

% Animar reconstrucción del contorno
for k = 1:N
    % Suma parcial de la serie de Fourier
    x_recon = real(ifft(X(1:k), N));
    y_recon = real(ifft(Y(1:k), N));

    % Limpiar la figura y dibujar el contorno actual
    clf;
    plot(x_recon, y_recon, 'b-', 'LineWidth', 2);
    title(sprintf('Reconstrucción con %d términos de Fourier', k));
    drawnow;
    pause(0.5); % Pausa para visualizar la animación
end
