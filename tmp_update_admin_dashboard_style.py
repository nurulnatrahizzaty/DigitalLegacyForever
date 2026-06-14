from pathlib import Path
import re

path = Path(r'c:\Users\5480\Documents\LEGACY_DIGITAL_FOREVER_PROTOTYP\LEGACY_DIGITAL_FOREVER_PROTOTYP\templates\admin_dashboard.html')
text = path.read_text(encoding='utf-8')
new_css = '''<style>
  .dashboard-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 24px 16px 40px;
  }

  .page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    margin-bottom: 36px;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(118, 0, 188, 0.12);
  }

  .page-title {
    font-size: 2.2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #7600bc 0%, #9333ea 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 6px;
    letter-spacing: -0.8px;
  }

  .page-description {
    color: #6b7280;
    font-size: 0.95rem;
    line-height: 1.7;
  }

  .header-buttons,
  .header-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }

  .btn {
    padding: 12px 22px;
    background: white;
    border: 1px solid rgba(118, 0, 188, 0.18);
    border-radius: 16px;
    font-size: 0.95rem;
    font-weight: 700;
    color: #334155;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    text-decoration: none;
  }

  .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 16px 30px rgba(118, 0, 188, 0.12);
    border-color: rgba(118, 0, 188, 0.28);
  }

  .btn-primary {
    background: linear-gradient(135deg, #7600bc 0%, #9333ea 100%);
    color: white;
    border-color: transparent;
  }

  .btn-secondary {
    background: white;
  }

  .notification-badge {
    position: absolute;
    top: -8px;
    right: -8px;
    width: 24px;
    height: 24px;
    display: grid;
    place-items: center;
    border-radius: 999px;
    background: #ef4444;
    color: white;
    font-size: 11px;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(239, 68, 68, 0.25);
  }

  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 20px;
    margin-bottom: 32px;
  }

  .kpi {
    position: relative;
    padding: 28px 24px;
    background: linear-gradient(180deg, #ffffff 0%, #f8f4ff 100%);
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid rgba(118, 0, 188, 0.12);
    box-shadow: 0 18px 32px rgba(118, 0, 188, 0.08);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }

  .kpi:hover {
    transform: translateY(-4px);
    box-shadow: 0 24px 45px rgba(118, 0, 188, 0.12);
  }

  .kpi::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #7600bc 0%, #9333ea 45%, #ec4899 100%);
  }

  .kpi .label {
    font-size: 12px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-weight: 700;
    color: #6366f1;
    margin-bottom: 10px;
  }

  .kpi .value {
    font-size: 3.1rem;
    font-weight: 900;
    color: #111827;
    margin-bottom: 16px;
    line-height: 1;
  }

  .kpi .badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 700;
  }

  .kpi .badge.positive {
    background: #dbeafe;
    color: #1d4ed8;
  }

  .kpi .badge.warning {
    background: #fee2e2;
    color: #b91c1c;
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 24px;
    margin-bottom: 32px;
  }

  .card {
    background: white;
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 24px 48px rgba(15, 23, 42, 0.06);
    border: 1px solid rgba(118, 0, 188, 0.1);
  }

  .card-heading {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 22px;
  }

  .card-heading strong {
    font-size: 1.1rem;
    color: #111827;
  }

  .card-heading small {
    color: #6b7280;
  }

  .status-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    margin-top: 16px;
  }

  .status-card {
    padding: 18px;
    border-radius: 22px;
    background: #f8f4ff;
    border: 1px solid rgba(118, 0, 188, 0.14);
  }

  .status-card .status-label {
    font-size: 11px;
    color: #6b7280;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 10px;
  }

  .status-card .status-value {
    font-size: 1.5rem;
    font-weight: 800;
    color: #111827;
  }

  .status-card .status-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: 10px;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 700;
    color: #7c3aed;
    background: rgba(124, 58, 237, 0.12);
  }

  .table-wrap {
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
  }

  table thead {
    background: linear-gradient(135deg, #7600bc 0%, #9333ea 100%);
  }

  table thead th {
    padding: 16px 18px;
    text-align: left;
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: white;
  }

  table tbody tr {
    border-bottom: 1px solid #eef2ff;
  }

  table tbody td {
    padding: 16px 18px;
    color: #334155;
    font-size: 0.95rem;
    vertical-align: middle;
  }

  table tbody td strong {
    color: #0f172a;
  }

  .empty-state {
    text-align: center;
    padding: 52px 20px;
    color: #94a3b8;
  }

  .empty-state i {
    font-size: 52px;
    margin-bottom: 14px;
    display: inline-block;
    opacity: 0.2;
  }

  @media (max-width: 1024px) {
    .dashboard-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 700px) {
    .page-header {
      flex-direction: column;
      align-items: flex-start;
    }

    .kpi-grid {
      grid-template-columns: 1fr;
    }

    .status-grid {
      grid-template-columns: 1fr;
    }

    .header-buttons,
    .header-actions {
      width: 100%;
      justify-content: flex-start;
    }
  }

  a {
    text-decoration: none;
    color: inherit;
  }
</style>'''
new_text = re.sub(r'<style>.*?</style>', new_css, text, flags=re.S)
if new_text == text:
    raise RuntimeError('style block replacement failed')
path.write_text(new_text, encoding='utf-8')
print('style block replaced')
